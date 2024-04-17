import cv2
import os
from tkinter import messagebox, Tk, Entry, Button
import threading
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def face_cropped(img):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame, 1.3, 5)
    
    cropped_faces = [cv2.resize(img[y:y+h, x:x+w], (450, 450)) for (x, y, w, h) in faces]
    return cropped_faces

def capture_images(cap, student_name):
    img_id = 0
    skip_frames = 5
    for _ in range(skip_frames):
        cap.read()  # Skip frames

    while img_id < 100:
        ret, my_frame = cap.read()
        faces = face_cropped(my_frame)

        for face in faces:
            img_id += 1
            folder_name = f"data/{student_name}"
            os.makedirs(folder_name, exist_ok=True)
            file_path = os.path.join(folder_name, f"{student_name}_{img_id}.jpg")

            threading.Thread(target=cv2.imwrite, args=(file_path, face)).start()

            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            cv2.imshow("Capture Images", face)

        if cv2.waitKey(1) & 0xFF == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Result", "Generating dataset completed!")

def start_capture():
    student_name = entry.get()
    
    if not student_name:
        messagebox.showwarning("Warning", "Please enter a student name.")
        return

    try:
        
        cap = cv2.VideoCapture(0)
        skip_frames = 5  # Adjust as needed

        capture_thread = threading.Thread(target=capture_images, args=(cap, student_name))
        capture_thread.start()

    except Exception as es:
        messagebox.showerror("Error", f"Due to: {str(es)}")

# Tkinter GUI
root = Tk()
root.title("Student Name Entry")

entry = Entry(root, width=30)
entry.pack(pady=10)

start_button = Button(root, text="Start Capture", command=start_capture)
start_button.pack(pady=10)

root.mainloop()
