def enroll_fingerprint():
    try:
        # connect to sensor
        f = pfp('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000) # change port later
    except Exception as e:
        print('sensor not found:', e)
    # scan fingerprint twice
    print('place your finger on the sensor...')
    while not f.readImage():
        pass
    f.convertImage(0x01)
    print('please remove your finger...')
    while f.readImage():
        pass
    print('place the same finger on the sensor...')
    while not f.readImage():
        pass
    f.convertImage(0x02)
    # compare & make sure the prints match
    if f.compareCharacteristics() == 0:
        print('fingers did not match, try again')
        return
    # store template on sensor memory
    f.createTemplate()
    positionNumber = f.storeTemplate()
    # note down position number
    print(f"fingerprint enrolled at position {positionNumber}!")