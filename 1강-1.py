import tkinter as tk
from tkinter import messagebox


def say_hello():
    # 버튼 클릭 시 메시지 박스 팝업 출력
    messagebox.showinfo("인사", "안녕하세요")


# 메인 윈도우 생성
root = tk.Tk()
root.title("인사하기 프로그램")
root.geometry("300x200")

# 버튼 생성 (클릭 시 say_hello 함수 연결)
btn = tk.Button(root, text="인사하기", font=("맑은 고딕", 12), command=say_hello)
btn.pack(expand=True)

# 이벤트 루프 실행
root.mainloop()