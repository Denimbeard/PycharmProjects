att = 'bbaccb'


class rec:
    a = 'a'
    b = 'b'
    c = 'c'
    i = 0
    x = 1
    cd = str(att[i])
    
    def fx():
        rec.x = rec.x + 1
        print(rec.i, rec.x, rec.cd)

    def fi():
        rec.i = rec.i + 1
        print(rec.i, rec.x, rec.cd)

    def bx():
        rec.x = rec.x - 1
        print(rec.i, rec.x, rec.cd)

    def sx():
        rec.x = rec.x + 0
        print(rec.i, rec.x, rec.cd)

    def fail():
        print('False','\n','Goodbye')
        quit()

    def pas():
        print('True\n', 'Goodbye\n')
        quit()

    def forward1():
        rec.fx()
        rec.fi()

    def stepback():
        rec.bx()
        rec.fi()

    def stepback2():
        rec.x = rec.x - 2
        rec.fi()

    def standstill():
        rec.sx()
        rec.fi()
    
    def steps(object): 
        while rec.x > 0:
            print(rec.i, rec.x, rec.cd)
            while rec.x == 1:
                print(rec.i, rec.x, rec.cd)
                if rec.cd == rec.b:
                    rec.forward1()
                if rec.cd == rec.c:
                    rec.forward1()
            else:
                rec.fail()
            
                while rec.x == 2:
                    print(rec.i, rec.x, rec.cd)
                    if rec.cd == rec.a:
                        rec.stepback()
                    if rec.cd == rec.b:
                        rec.forward1()
                else:
                    rec.fail()
                    while rec.x == 3:
                        print(rec.i, rec.x, rec.cd)
                        if rec.cd == rec.a:
                            rec.forward1()
                    else:
                        rec.fail()
                        
                        while rec.x == 4:
                            print(rec.i, rec.x, rec.cd)
                            if rec.cd == rec.a:
                                rec.standstill()
                            if rec.cd == rec.b:
                                rec.stepback()
                            if rec.cd == rec.c:
                                rec.forward1()
                        else:
                            rec.fail()
                            while rec.x == 5:
                                print(rec.i, rec.x, rec.cd)
                                if rec.cd == rec.b:
                                    rec.stepback2()
                                if rec.cd == rec.c:
                                    rec.forward1()
                            else:
                                rec.fail()
                                while rec.x == 6:
                                    print(rec.i, rec.x, rec.cd)
                                    if rec.cd == rec.a:
                                        rec.stepback()
                                    if rec.cd == rec.b:
                                        rec.forward()
                                    if rec.cd == rec.c:
                                        rec.standstill()
                                else:
                                    rec.fail()
                                    while rec.x == 7:
                                            print(rec.i, rec.x, rec.cd)
                                            pas()
        else:
            rec.fail()

