import flet as ft

def main(page: ft.Page):
    page.title = "لوحة التحكم والسيطرة الشاملة"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.DARK

    # حقول إدخال قسم الروابط
    link_input = ft.TextField(label="أدخل اسم الرابط أو الهدف", width=350)
    output_view = ft.Text("لم يتم إنشاء أي رابط بعد.", selectable=True)

    # حقول إدخال قسم التحكم والإشعارات
    control_output = ft.Text("سجل الأحداث والإشعارات فارغ حالياً.", color=ft.colors.YELLOW)

    # دالة إنشاء الرابط
    def generate_link(e):
        val = link_input.value
        if not val:
            page.show_snack_bar(ft.SnackBar(ft.Text("الرجاء إدخال بيانات صالحة!")))
            return
        
        tracking_url = f"https://example.com/target?q={val.replace(' ', '_')}"
        output_view.value = f"الرابط النشط:\n{tracking_url}"
        control_output.value = f"تم إنشاء رابط جديد لـ: [{val}] في انتظار التفاعل..."
        page.update()

    # محتوى التبويب الأول: الروابط والإنشاء
    tab1_content = ft.Column([
        ft.Text("إدارة وصنع الروابط", size=18, weight=ft.FontWeight.BOLD),
        link_input,
        ft.ElevatedButton("إنشاء رابط تعقب", on_click=generate_link),
        output_view
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # محتوى التبويب الثاني: لوحة الإشعارات والتحكم
    tab2_content = ft.Column([
        ft.Text("الإشعارات وسجل التحكم", size=18, weight=ft.FontWeight.BOLD),
        control_output,
        ft.ElevatedButton("تحديث الحالة وجلب التنبيهات", on_click=lambda e: page.update())
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # تصميم التبويبات (Tabs) لتنقل سلس داخل التطبيق
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="الروابط", content=tab1_content),
            ft.Tab(text="التحكم والإشعارات", content=tab2_content),
        ],
        expand=1
    )

    page.add(tabs)

ft.app(target=main)

