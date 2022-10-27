def cal_bmi(height,weight):
    print ("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    print("BMI = " + str(bmi))

    if bmi<18.5:
        print("Under weight")
    elif bmi>=18.5 or bmi<=25:
        print("Normal weight")
    else:
        print("Over weight")


cal_bmi(weight=57,height=1.73)
