# Gianna_Ride_Receipt_Aug_8_2025.
Gianna_Ride_Receipt_Aug_8_2025.
from fpdf import FPDF

# Create a PDF receipt
class RideReceiptPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(40, 40, 40)
        self.cell(0, 10, "Ride Booking Confirmation", ln=True, align="C")
        self.ln(5)

    def add_section(self, title, content):
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(30, 30, 30)
        self.cell(40, 10, f"{title}:", ln=0)
        self.set_font("Helvetica", "", 12)
        self.set_text_color(50, 50, 50)
        self.cell(100, 10, f"{content}", ln=1)

# Generate the PDF
pdf = RideReceiptPDF()
pdf.add_page()

# Add booking details
pdf.set_font("Helvetica", "", 12)
pdf.add_section("Passenger Name", "Gianna")
pdf.add_section("Pickup Address", "Corona, CA")
pdf.add_section("Drop-off Address", "6343 Mykonos Ln, Riverside, CA")
pdf.add_section("Date", "August 8, 2025")
pdf.add_section("Time", "10:00 AM PT")
pdf.add_section("Status", "Confirmed")
pdf.add_section("Booking ID", "#RBK-08921")
pdf.add_section("Ride Service", "SoCal Express Rides")

# Save the file
pdf.output("Gianna_Ride_Receipt_Aug_8_2025.pdf")