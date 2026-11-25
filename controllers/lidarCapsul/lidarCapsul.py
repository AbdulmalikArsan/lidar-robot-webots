from controller import Robot

#robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

#Motor roda
motor_kanan = robot.getDevice('motor_kanan')
motor_kiri = robot.getDevice('motor_kiri')
motor_kanan.setPosition(float('inf'))
motor_kiri.setPosition(float('inf'))

#Lidar
lidar = robot.getDevice('lidar')
lidar.enable(timestep)

MAX_SPEED = 6.28

while robot.step(timestep) != -1:
    #Jarak dari lidar
    range_image = lidar.getRangeImage()
    lebar = lidar.getHorizontalResolution()
    

    
    #Membagi lidar 3 bagian
    sepertiga = lebar // 3
    
    bagian_kanan  = range_image[0 : sepertiga]
    bagian_depan = range_image[sepertiga : 2 * sepertiga]
    bagian_kiri = range_image[2 * sepertiga : lebar]
    
    #Jarak valid
    def get_min_dist(sector):
        valid_vals = [val for val in sector if val != float('inf')]
        return min(valid_vals) if valid_vals else 10.0 #meter
    
    jarak_kanan  = get_min_dist(bagian_kanan)
    jarak_depan = get_min_dist(bagian_depan)
    jarak_kiri = get_min_dist(bagian_kiri)
    
    #Cetak status ke terminal
    print(f"[LIDAR] Kanan: {jarak_kanan:.2f}m | Depan: {jarak_depan:.2f}m | Kiri: {jarak_kiri:.2f}m")
    
    
    SAFE_DISTANCE = 0.5 #meter
    
    if jarak_depan < SAFE_DISTANCE:
        #Jika ada rintangan di depan, putar ke arah yang lebih aman
        if jarak_kanan > jarak_kiri:
            #Putar ke kanan
            motor_kanan.setVelocity(-MAX_SPEED * 0.5)
            motor_kiri.setVelocity(MAX_SPEED * 0.5)
            print("[AKSI] Rintangan di depan. Memutar ke kanan.")
        elif jarak_kiri > jarak_kanan:
            #Putar ke kiri
            motor_kanan.setVelocity(MAX_SPEED * 0.5)
            motor_kiri.setVelocity(-MAX_SPEED * 0.5)
            print("[AKSI] Rintangan di depan. Memutar ke kiri.")
            
    if jarak_depan < SAFE_DISTANCE and jarak_kanan < SAFE_DISTANCE and jarak_kiri < SAFE_DISTANCE:
        motor_kanan.setVelocity(MAX_SPEED)
        motor_kiri.setVelocity(-MAX_SPEED)
        print("[AKSI] Memutar")


    elif jarak_kiri < SAFE_DISTANCE:
        #Jika ada rintangan di kiri, putar ke kanan
        motor_kanan.setVelocity(MAX_SPEED * 0.2)
        motor_kiri.setVelocity(MAX_SPEED * 0.5)
        print("[AKSI] Rintangan di kiri. Memutar ke kanan.")

    elif jarak_kanan < SAFE_DISTANCE:
        #Jika ada rintangan di kanan, putar ke kiri
        motor_kanan.setVelocity(MAX_SPEED * 0.5)
        motor_kiri.setVelocity(MAX_SPEED * 0.2)
        print("[AKSI] Rintangan di kanan. Memutar ke kiri.")

    elif jarak_depan >= SAFE_DISTANCE:
        #Berjalan maju lurus
        motor_kanan.setVelocity(MAX_SPEED * 1)
        motor_kiri.setVelocity(MAX_SPEED * 1)
        print("[AKSI] Jalur aman. Berjalan maju.")
    