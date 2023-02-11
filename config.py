import obj as o


def get_test_board():
    """Retursn a test board"""
    # make a test board

    #row 1
    b = o.Board()
    b.set_square(1,6,8,"Bill")
    b.set_square(2,6,1,"Monica")
    b.set_square(3,6,4,"Steve B")
    b.set_square(4,6,0,"Mac")
    b.set_square(5,6,6,"Juliette Thut")
    b.set_square(6,6,5,"Freddy H.")
    b.set_square(7,6,7,"Curtis S.")
    b.set_square(8,6,2,"Sev Z")
    b.set_square(9,6,9,"Jamie L")
    b.set_square(10,6,3,"Jeenette")

    #row 2
    b.set_square(11,4,8,"Monica")
    b.set_square(12,4,1,"Jamie L")
    b.set_square(13,4,4,"TRM")
    b.set_square(14,4,0,"Seve B")
    b.set_square(15,4,6,"Tom Hodge")
    b.set_square(16,4,5,"Bill")
    b.set_square(17,4,7,"Nick P")
    b.set_square(18,4,2,"Bill B")
    b.set_square(19,4,9,"Jenette")
    b.set_square(20,4,3,"Wilson")


    #row 3
    b.set_square(21,2,8,"MCM")
    b.set_square(22,2,1,"Jackie Thut")
    b.set_square(23,2,4,"Tom Hodge")
    b.set_square(24,2,0,"Bill")
    b.set_square(25,2,6,"Steve B")
    b.set_square(26,2,5,"Will Seigs")
    b.set_square(27,2,7,"Monica")
    b.set_square(28,2,2,"Jen N")
    b.set_square(29,2,9,"Sevs")
    b.set_square(30,2,3,"Curtis S")


    #row 4
    b.set_square(31,5,8,"Curtis S.")
    b.set_square(32,5,1,"Donny J.")
    b.set_square(33,5,4,"Evie Steigs")
    b.set_square(34,5,0,"Tyler Thut")
    b.set_square(35,5,6,"Jamie L")
    b.set_square(36,5,5,"Steve B")
    b.set_square(37,5,7,"Bill")
    b.set_square(38,5,2,"EGM")
    b.set_square(39,5,9,"Monica")
    b.set_square(40,5,3,"Alice")


    #row 5
    b.set_square(41,1,8,"MAC")
    b.set_square(42,1,1,"Danny H.")
    b.set_square(43,1,4,"WRM")
    b.set_square(44,1,0,"Johnny Stengs")
    b.set_square(45,1,6,"Curtis S.")
    b.set_square(46,1,5,"Jeff Thut")
    b.set_square(47,1,7,"AJ Thut")
    b.set_square(48,1,2,"Bill")
    b.set_square(49,1,9,"Wilson")
    b.set_square(50,1,3,"Monica")

    #row 6
    b.set_square(51,3,8,"Bhesoh H.")
    b.set_square(52,3,1,"Jen N")
    b.set_square(53,3,4,"Megan McKown")
    b.set_square(54,3,0,"Jackson Thut")
    b.set_square(55,3,6,"Naomis Thut Kid")
    b.set_square(56,3,5,"Tom HOdge")
    b.set_square(57,3,7,"Mac")
    b.set_square(58,3,2,"Monica")
    b.set_square(59,3,9,"Shea Steigs")
    b.set_square(60,3,3,"Bill")

    #row 7
    b.set_square(71,9,8,"Danny H.")
    b.set_square(72,9,1,"Macky Thut")
    b.set_square(73,9,4,"Shea S. Thut Kid")
    b.set_square(74,9,0,"Monica")
    b.set_square(75,9,6,"Bill B")
    b.set_square(76,9,5,"Jacks")
    b.set_square(77,9,7,"Meg Steigs")
    b.set_square(78,9,2,"Marty")
    b.set_square(79,9,9,"Bill")
    b.set_square(80,9,3,"SBG")

    #row 8
    b.set_square(71,8,8,"Nick P")
    b.set_square(72,8,1,"Mark Y")
    b.set_square(73,8,4,"Monica")
    b.set_square(74,8,0,"Merb B")
    b.set_square(75,8,6,"Bill")
    b.set_square(76,8,5,"Bryson H")
    b.set_square(77,8,7,"Wilson")
    b.set_square(78,8,2,"Tom Hodge")
    b.set_square(79,8,9,"SBG")
    b.set_square(80,8,3,"Nick P")


    #row 9
    b.set_square(81,7,8,"Wilson")
    b.set_square(82,7,1,"Fready H")
    b.set_square(83,7,4,"Bill")
    b.set_square(84,7,0,"Curtis s.")
    b.set_square(85,7,6,"Alyson")
    b.set_square(86,7,5,"Monica")
    b.set_square(87,7,7,"Bill B")
    b.set_square(88,7,2,"Kelly Thut")
    b.set_square(89,7,9,"JRN")
    b.set_square(90,7,3,"Jeff Thut")


    #row 10
    b.set_square(91,0,8,"Mac")
    b.set_square(92,0,1,"Bill")
    b.set_square(93,0,4,"Rebecca")
    b.set_square(94,0,0,"Bill B")
    b.set_square(95,0,6,"Monica")
    b.set_square(96,0,5,"Nick P")
    b.set_square(97,0,7,"Jamie L")
    b.set_square(98,0,2,"Guy")
    b.set_square(99,0,9,"Jennifer")
    b.set_square(100,0,3,"Greg")


    return b
