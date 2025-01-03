import sys
import os
import customtkinter as ctk
from tkinter import filedialog, messagebox
from meta_extractor import analyze_text, export_results

last_result = None 

def show_popup(title, message, file_name=None, is_error=False):
    """Create a pop-up window to display analysis results or error messages."""
    popup = ctk.CTkToplevel()
    popup.title(title)
    popup.geometry("500x400")
    popup.resizable(True, True)

    popup_label = ctk.CTkLabel(
        popup,
        text=f"{title}{f' - {file_name}' if file_name else ''}",
        font=("Arial", 16, "bold"),
        text_color="red" if is_error else "white",
    )
    popup_label.pack(pady=10)

    text_box = ctk.CTkTextbox(popup, wrap="word", state="normal", font=("Arial", 14))
    text_box.pack(padx=10, pady=10, fill="both", expand=True)

    text_box.insert("1.0", message)
    text_box.configure(state="disabled")

    def save_results():
        """Save results to a file if the Text area is not empty."""
        # Ensure the text box has content before proceeding
        content = text_box.get("1.0", "end").strip()  # Get text and remove whitespace
        if content:  # Check if there's any content
            output_file = filedialog.asksaveasfilename(
                title="Save Results As",
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if output_file:
                try:
                    with open(output_file, 'w', encoding='utf-8') as file:
                        file.write(content)  # Write the content to the file
                    messagebox.showinfo("Success", f"Results saved to {output_file}")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not save results: {str(e)}")
        else:
            # Show a message if the text box is empty
            messagebox.showinfo("No Content", "The results area is empty. Nothing to save.")


    save_button = ctk.CTkButton(popup, text="Save Results", command=save_results, fg_color="green")
    save_button.pack(pady=5)

    close_button = ctk.CTkButton(popup, text="Close", command=popup.destroy, fg_color="gray")
    close_button.pack(pady=10)

    popup.grab_set()


def analyze_file():
    """Handle file selection and perform analysis."""
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("All Supported Files", "*.txt *.docx *.pdf *.rtf *.odt *.html"),
            ("Text Files", "*.txt"),
            ("Word Files", "*.docx"),
            ("PDF Files", "*.pdf"),
            ("Rich Text Format", "*.rtf"),
            ("Open Document Text", "*.odt"),
            ("HTML Files", "*.html"),
            ("All Files", "*.*")
        ]
    )
    if file_path:
        try:
            result = analyze_text(file_path)
            file_name = os.path.basename(file_path)
            if isinstance(result, dict):
                result_text = "\n".join([f"{key}: {value}" for key, value in result.items()])
                show_popup("Analysis Results", result_text, file_name=file_name)
            else:
                show_popup("Error", result, file_name=file_name, is_error=True)
        except Exception as e:
            show_popup("Error", str(e), file_name=os.path.basename(file_path), is_error=True)


def export_last_results():
    """Export the results of the last analysis."""
    if 'last_result' in globals() and last_result:
        output_file = filedialog.asksaveasfilename(
            title="Save Results As",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if output_file:
            try:
                export_results(last_result, output_file)
                messagebox.showinfo("Success", f"Results saved to {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save results: {str(e)}")
    else:
        messagebox.showwarning("No Results", "No analysis results available to export.")


# GUI Setup
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Document Analyzer")
root.geometry("500x500")
root.resizable(True, True)

label = ctk.CTkLabel(root, text="Welcome to the Document Analyzer Tool", font=("Arial", 18, "bold"))
label.pack(pady=10)

analyze_button = ctk.CTkButton(root, text="Analyze a File", command=analyze_file, fg_color="blue")
analyze_button.pack(pady=20)

quit_button = ctk.CTkButton(root, text="Quit", command=root.quit, fg_color="red")
quit_button.pack(pady=10)

root.mainloop()
