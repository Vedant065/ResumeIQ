import { CheckCircle, XCircle } from "lucide-react";

interface Section {
  name: string;
  present: boolean;
}

interface Props {
  sections: Section[];
}

export default function SectionAnalysisCard({ sections }: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-xl">
      <h2 className="mb-6 text-xl font-bold">
        📋 Resume Section Analysis
      </h2>

      <div className="space-y-4">
        {sections.map((section) => (
          <div
            key={section.name}
            className="flex items-center justify-between rounded-lg bg-slate-50 p-3"
          >
            <span className="font-medium">{section.name}</span>

            {section.present ? (
              <div className="flex items-center gap-2 text-green-600">
                <CheckCircle size={20} />
                Present
              </div>
            ) : (
              <div className="flex items-center gap-2 text-red-600">
                <XCircle size={20} />
                Missing
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}