
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Output PDF file
file_path = "escort_driver_booking_receipt.pdf"

# Create PDF
doc = SimpleDocTemplate(file_path, pagesize=LETTER)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("<b>ESCORT DRIVER SERVICE – BOOKING RECEIPT</b>", styles["Title"]))
elements.append(Spacer(1, 12))

# Booking info
elements.append(Paragraph("<b>Booking Confirmation Number:</b> 2025-08-08-001", styles["Normal"]))
elements.append(Paragraph("<b>Date Issued:</b> August 8, 2025", styles["Normal"]))
elements.append(Spacer(1, 12))

# Pickup details table
pickup_data = [
    ["<b>Pickup Details</b>", ""],
    ["Passenger Name:", "Gianna"],
    ["Pickup Location:", "Corona, CA"],
    ["Pickup Date/Time:", "__________________"]
]
pickup_table = Table(pickup_data, colWidths=[150, 300])
pickup_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.black),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
]))
elements.append(pickup_table)
elements.append(Spacer(1, 12))

# Drop-off details table
dropoff_data = [
    ["<b>Drop-off Details</b>", ""],
    ["Arrival Address:", "6343 Mykonos Ln, Riverside, CA"]
]
dropoff_table = Table(dropoff_data, colWidths=[150, 300])
dropoff_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.black),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
]))
elements.append(dropoff_table)
elements.append(Spacer(1, 12))

# Service info table
service_data = [
    ["<b>Service Information</b>", ""],
    ["Service Type:", "Private Escort Driver – One Way Trip"],
    ["Driver Name:", "__________________"],
    ["Vehicle Type/Plate:", "__________________"],
    ["Total Fare:", "$_________"],
    ["Payment Method:", "__________________"]
]
service_table = Table(service_data, colWidths=[150, 300])
service_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.black),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
]))
elements.append(service_table)
elements.append(Spacer(1, 12))

# Notes
elements.append(Paragraph("<b>Notes:</b>", styles["Heading4"]))
elements.append(Paragraph("• Please be ready at the pickup location at least 5 minutes before the scheduled time.", styles["Normal"]))
elements.append(Paragraph("• For changes or cancellations, contact dispatch immediately.", styles["Normal"]))
elements.append(Spacer(1, 20))

# Signature area
elements.append(Paragraph("<b>Authorized By:</b> __________________", styles["Normal"]))
elements.append(Paragraph("<b>Company/Dispatch Contact:</b> __________________", styles["Normal"]))

# Build PDF
doc.build(elements)

print(f"Receipt PDF created: {file_path}")
