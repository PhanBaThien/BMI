import tkinter as tk
from tkinter import ttk, messagebox
from Model.person import Person
from services.bmi_service import BMIService

class BMIView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI Calculator")
        self.root.geometry("500x600")
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Configure style
        style = ttk.Style()
        style.configure("TLabel", padding=5, font=('Helvetica', 12))
        style.configure("TEntry", padding=5)
        style.configure("TButton", padding=5, font=('Helvetica', 12))
        
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(
            self.main_frame, 
            text="BMI Calculator", 
            font=('Helvetica', 24, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Input fields
        self.create_input_fields()
        
        # Calculate button
        calculate_button = ttk.Button(
            self.main_frame, 
            text="Tính BMI", 
            command=self.calculate_bmi
        )
        calculate_button.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Result area
        self.result_frame = ttk.LabelFrame(
            self.main_frame, 
            text="Kết quả", 
            padding="10"
        )
        self.result_frame.grid(row=6, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.result_label = ttk.Label(
            self.result_frame, 
            text="", 
            font=('Helvetica', 14),
            wraplength=400
        )
        self.result_label.grid(row=0, column=0, pady=10)
        
        # Configure grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        for i in range(7):
            self.main_frame.grid_rowconfigure(i, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        
    def create_input_fields(self):
        """Create input fields for user data"""
        # Name field
        ttk.Label(self.main_frame, text="Tên:").grid(row=1, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(self.main_frame, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)
        
        # Age field
        ttk.Label(self.main_frame, text="Tuổi:").grid(row=2, column=0, sticky=tk.W)
        self.age_entry = ttk.Entry(self.main_frame, width=30)
        self.age_entry.grid(row=2, column=1, pady=5)
        
        # Height field
        ttk.Label(self.main_frame, text="Chiều cao (m):").grid(row=3, column=0, sticky=tk.W)
        self.height_entry = ttk.Entry(self.main_frame, width=30)
        self.height_entry.grid(row=3, column=1, pady=5)
        
        # Weight field
        ttk.Label(self.main_frame, text="Cân nặng (kg):").grid(row=4, column=0, sticky=tk.W)
        self.weight_entry = ttk.Entry(self.main_frame, width=30)
        self.weight_entry.grid(row=4, column=1, pady=5)
        
    def calculate_bmi(self):
        """Calculate BMI and display results"""
        try:
            # Get input values
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            
            # Create person object and calculate BMI
            person = Person(name, age, height, weight)
            bmi = BMIService.calculate_bmi(person)
            category = BMIService.classify_bmi(person)
            advice = BMIService.get_bmi_advice(person)
            
            # Display results
            result_text = f"{person}\n\nLời khuyên: {advice}"
            self.result_label.config(text=result_text)
            
        except ValueError:
            messagebox.showerror(
                "Lỗi", 
                "Vui lòng nhập đúng định dạng số cho tuổi, chiều cao và cân nặng!"
            )
            
    def run(self):
        """Start the application"""
        self.root.mainloop() 