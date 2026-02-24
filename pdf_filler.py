from reportlab.pdfgen import canvas

def generate_pdf(user, scheme):
    filename = f"{scheme['name'].replace(' ', '_')}.pdf"
    c = canvas.Canvas(filename)

    c.drawString(100, 750, "Government Scheme Application")
    c.drawString(100, 720, f"Name: {user['name']}")
    c.drawString(100, 700, f"Income: ₹{user['income']}")
    c.drawString(100, 680, f"Scheme: {scheme['name']}")
    c.drawString(100, 660, f"Benefit: {scheme['benefit']}")

    c.save()
    return filename