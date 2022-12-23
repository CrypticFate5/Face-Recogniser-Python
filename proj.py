import cv2
import tkinter as tk


def facedetect():
    face_Cascade = cv2.CascadeClassifier("hc_ff.xml")
    cap = cv2.VideoCapture(0)
    cap.set(10, 100)
    while cap.isOpened():
        _ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_Cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "FACE", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, 2)
        cv2.imshow("Face Detect", frame)
        if cv2.waitKey(40) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def eyedetect():
    eye_Cascade = cv2.CascadeClassifier("eye.xml")
    cap = cv2.VideoCapture(0)
    cap.set(10, 100)
    while cap.isOpened():
        _ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_Cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "EYE", (x, y),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, 2)
        cv2.imshow("Eye Detect", frame)
        if cv2.waitKey(40) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def show_this_code():
    root = tk.Tk()
    root.title("CODE")
    root.geometry("1920x1080")
    bg = tk.PhotoImage(file="imgg.png")
    my_label = tk.Label(root)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)

    my_text = tk.Label(root, text="""import cv2
import tkinter as tk


def facedetect():
    face_Cascade = cv2.CascadeClassifier("hc_ff.xml")
    cap = cv2.VideoCapture(0)
    cap.set(10, 100)
    while cap.isOpened():
        _ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_Cascade.detectMultiScale(gray, 1.1, 4)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) 
            cv2.putText(frame, "FACE", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2, 2)
        cv2.imshow("Face Detect", frame)
        if cv2.waitKey(40) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

    
def eyedetect():
    eye_Cascade = cv2.CascadeClassifier("eye.xml")
    cap = cv2.VideoCapture(0)
    cap.set(10, 100)
    while cap.isOpened():
        _ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_Cascade.detectMultiScale(gray, 1.1, 4)
        for (x,y,w,h) in eyes:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) 
            cv2.putText(frame, "EYE", (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2, 2)
        cv2.imshow("Eye Detect", frame)
        if cv2.waitKey(40) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
def show_this_code():
    ...

root = tk.Tk()
root.title("PYTHON MINI PROJECT")
root.geometry("1920x1080")
bg = tk.PhotoImage(file="imgg.png")
my_label = tk.Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

my_text = tk.Label(root, text="Face and Eye Detector", font=("Jocker", 50), fg="white",bg="black")
my_text.pack(pady=50)

my_button1 = tk.Button(my_label, text="Face Detector" ,command=facedetect ,fg="white", bg="black", font=("Algerian" ,15) , padx=40 , pady=10 , borderwidth=7)
my_button1.grid(row=0, column=1, padx=10 , pady=250)
my_button1.place(x=450,y=170)

my_button2 = tk.Button(my_label, text="Eye Detector" ,command=eyedetect ,fg="white", bg="black", font=("Algerian" ,15) , padx=40 , pady=10 , borderwidth=7)
my_button2.grid(row=0, column=1, padx=10 , pady=250)
my_button2.place(x=750,y=170)

my_button3 = tk.Button(my_label, text="Show This Code",command=show_this_code,fg="white", bg="black",font=("Algerian" ,15), padx=40 , pady=10 , borderwidth=7)
my_button3.grid(row=0, column=3, padx=10 , pady=250 )
my_button3.place(x=575,y=600)

my_button4 = tk.Button(my_label, text="Exit",command=root.quit,fg="white", bg="black",font=("Algerian" ,15), padx=40 , pady=10 , borderwidth=7)
my_button4.grid(row=0, column=4, padx=10 , pady=250 )
my_button4.place(x=630,y=700)

root.mainloop()
exit()
    """, font=("Jocker", 10), fg="white", bg="black")
    my_text.pack(pady=10)


root = tk.Tk()
root.title("PYTHON MINI PROJECT")
root.geometry("1920x1080")
bg = tk.PhotoImage(file="imgg.png")
my_label = tk.Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

my_text = tk.Label(root, text="Face and Eye Detector",
                   font=("Jocker", 50), fg="white", bg="black")
my_text.pack(pady=50)

my_button1 = tk.Button(my_label, text="Face Detector", command=facedetect,
                       fg="white", bg="black", font=("Algerian", 15), padx=40, pady=10, borderwidth=7)
my_button1.grid(row=0, column=1, padx=10, pady=250)
my_button1.place(x=450, y=170)

my_button2 = tk.Button(my_label, text="Eye Detector", command=eyedetect, fg="white",
                       bg="black", font=("Algerian", 15), padx=40, pady=10, borderwidth=7)
my_button2.grid(row=0, column=1, padx=10, pady=250)
my_button2.place(x=750, y=170)

my_button3 = tk.Button(my_label, text="Show This Code", command=show_this_code,
                       fg="white", bg="black", font=("Algerian", 15), padx=40, pady=10, borderwidth=7)
my_button3.grid(row=0, column=3, padx=10, pady=250)
my_button3.place(x=575, y=600)

my_button4 = tk.Button(my_label, text="Exit", command=root.quit, fg="white",
                       bg="black", font=("Algerian", 15), padx=40, pady=10, borderwidth=7)
my_button4.grid(row=0, column=4, padx=10, pady=250)
my_button4.place(x=630, y=700)

root.mainloop()
exit()
