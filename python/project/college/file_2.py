from file_1 import Student as st 
if (__name__ == "__main__"):
    st_1 = st("","","")
    while True:
        print("..... College .........".center(50))
        print("\n1.Add Student Details \n2.Show student details \n3.Check Result \n4. Add Result")
        opr = int(input())
        match opr:
            case 1:
                pass
            case 2: 
                st.show_details()
            case 3:
                pass
            case 4:
                pass
            case _:
                print("No Programe Found")
                break
                