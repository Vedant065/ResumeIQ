import jsPDF from "jspdf";

export function generateReport(result: any) {
  const doc = new jsPDF();

  let y = 20;

  doc.setFontSize(22);
  doc.text("ResumeIQ Analysis Report", 20, y);

  y += 15;

  doc.setFontSize(14);
  doc.text(`ATS Score: ${result.ats_score}%`, 20, y);

  y += 15;

  doc.text("Strengths:", 20, y);

  y += 10;

  result.strengths.forEach((item: string) => {
    doc.text(`• ${item}`, 25, y);
    y += 8;
  });

  y += 5;

  doc.text("Suggestions:", 20, y);

  y += 10;

  result.suggestions.forEach((item: string) => {
    doc.text(`• ${item}`, 25, y);
    y += 8;
  });

  y += 5;

  doc.text(`Job Match Score: ${result.match_score}%`, 20, y);

  y += 10;

  doc.text("Matched Skills:", 20, y);

  y += 10;

  result.matched_skills.forEach((skill: string) => {
    doc.text(`• ${skill}`, 25, y);
    y += 8;
  });

  y += 5;

  doc.text("Missing Skills:", 20, y);

  y += 10;

  result.missing_skills.forEach((skill: string) => {
    doc.text(`• ${skill}`, 25, y);
    y += 8;
  });

  doc.save("ResumeIQ_Report.pdf");
}