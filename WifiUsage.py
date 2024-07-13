import tkinter as tk
from tkinter import messagebox


def calculate_usage():
    try:
        paid_amount = float(paid_amount_entry.get())
        total_package_size = float(total_package_size_entry.get())
        num_users = int(num_users_entry.get())

        users_data = []
        for i in range(num_users):
            name = name_entries[i].get()
            consumption = float(consumption_entries[i].get())
            users_data.append((name, consumption))

        total_consumption = sum([consumption for name, consumption in users_data])
        remaining_package = total_package_size - total_consumption
        share_per_user_before = total_package_size / num_users
        share_per_user_after = paid_amount / (total_package_size - remaining_package)
        cost_per_gb = paid_amount / total_package_size
        payment_first = paid_amount / num_users
        size_befor = total_package_size - remaining_package
        final_size_for_all_user = size_befor / num_users
        result_text = (
            f"الفقد في الباقه: {remaining_package:.2f} جيجابايت\n"
            f"النصيب لكل مستخدم قبل الاستهلاك: {share_per_user_before:.2f} جيجابايت\n"
            f"الدفع عند تجديد الباقه لكل شخص: {payment_first:.2f} جنيه\n"
            f"حجم الباقه بعد الفقد: {size_befor:.2f} جيجابايت\n"
            f"حجم الاستهلاك المستحق بعد الفقد: {final_size_for_all_user:.2f} جيجابايت\n"
            f"سعر الجيجا في الباقه بعد الاستهلاك الكلي: {share_per_user_after:.2f} جنيه\n\n"
        )

        for name, consumption in users_data:
            cost = consumption * share_per_user_after
            cost_pay = final_size_for_all_user - consumption
            cost_pay2 = cost_pay * share_per_user_after
            result_text += (
                f'المستخدم: {name}\n'
                f'الاستهلاك: {consumption:.2f} جيجابايت\n'
                f'سعر الجيجا للاستهلاك: {share_per_user_after:.2f} جنيه\n'
                f'تكلفة الكليه الاستهلاك: {cost:.2f} جنيه\n'
                f'الجيجات المستحقه لك / عليك: {cost_pay:.2f} جيجابايت\n'
                f'المال المستحقه لك / عليك: {cost_pay2:.2f} جنيه\n\n'
            )

        result_window = tk.Toplevel(root)
        result_window.title("النتائج")

        text_box = tk.Text(result_window, wrap='word', width=80, height=20)
        text_box.pack(side='left', fill='both', expand=True)

        scrollbar = tk.Scrollbar(result_window, command=text_box.yview)
        scrollbar.pack(side='right', fill='y')

        text_box['yscrollcommand'] = scrollbar.set

        text_box.insert('end', result_text)
        text_box.config(state='disabled')

    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ: {e}")


def create_user_entries():
    try:
        num_users = int(num_users_entry.get())
        for widget in user_frame.winfo_children():
            widget.destroy()

        global name_entries, consumption_entries
        name_entries = []
        consumption_entries = []

        for i in range(num_users):
            tk.Label(user_frame, text=f"اسم المستخدم {i + 1}:").grid(row=i, column=0, padx=5, pady=5)
            name_entry = tk.Entry(user_frame)
            name_entry.grid(row=i, column=1, padx=5, pady=5)
            name_entries.append(name_entry)

            tk.Label(user_frame, text=f"استهلاك المستخدم {i + 1} (جيجابايت):").grid(row=i, column=2, padx=5, pady=5)
            consumption_entry = tk.Entry(user_frame)
            consumption_entry.grid(row=i, column=3, padx=5, pady=5)
            consumption_entries.append(consumption_entry)
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال عدد صحيح من المستخدمين.")


root = tk.Tk()
root.title("حساب استهلاك الواي فاي")

tk.Label(root, text="المبلغ المدفوع:").grid(row=0, column=0, padx=5, pady=5)
paid_amount_entry = tk.Entry(root)
paid_amount_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="حجم الباقة الكلي (جيجابايت):").grid(row=1, column=0, padx=5, pady=5)
total_package_size_entry = tk.Entry(root)
total_package_size_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="عدد المستخدمين:").grid(row=2, column=0, padx=5, pady=5)
num_users_entry = tk.Entry(root)
num_users_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="إنشاء إدخالات المستخدم", command=create_user_entries).grid(row=2, column=2, padx=5, pady=5)

user_frame = tk.Frame(root)
user_frame.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

tk.Button(root, text="حساب الاستهلاك", command=calculate_usage).grid(row=4, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
