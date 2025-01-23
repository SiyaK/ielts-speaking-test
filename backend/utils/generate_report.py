from fpdf import FPDF

def generate_pdf_report(transcript, feedback):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"IELTS Speaking Test Report\n\nTranscript:\n{transcript}\n\nFeedback:\n{feedback}")
    report_path = "reports/ielts_report.pdf"
    pdf.output(report_path)
    return report_path
