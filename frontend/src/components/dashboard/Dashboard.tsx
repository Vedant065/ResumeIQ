import ATSCard from "./ATSGauge";
import KeywordCard from "./KeywordCard";
import StrengthCard from "./StrengthCard";
import SuggestionCard from "./SuggestionCard";
import FeedbackCard from "./FeedbackCard";
import PreviewCard from "./PreviewCard";
import SectionAnalysisCard from "./SectionAnalysisCard";
import JobMatchCard from "./JobMatchCard";

import { Button } from "@/components/ui/button";
import { generateReport } from "@/utils/generateReport";

interface DashboardProps {
  result: any;
}

export default function Dashboard({ result }: DashboardProps) {
  return (
    <section className="mx-auto max-w-7xl px-6 py-10">
      <div className="space-y-6">

        {/* Download Report Button */}
        <div className="flex justify-end">
          <Button
            onClick={() => generateReport(result)}
            className="bg-green-600 hover:bg-green-700"
          >
            Download Report
          </Button>
        </div>

        {/* ATS Score */}
        <ATSCard score={result.ats_score} />

        {/* Two Column Layout */}
        <div className="grid gap-6 lg:grid-cols-2">
          <KeywordCard keywords={result.keywords_found} />

          <StrengthCard strengths={result.strengths} />

          <SuggestionCard suggestions={result.suggestions} />

          <FeedbackCard feedback={result.ai_feedback} />
        </div>

        {/* Resume Section Analysis */}
        <SectionAnalysisCard
          sections={result.section_analysis || []}
        />

        {/* Job Match */}
        <JobMatchCard
          matchScore={result.match_score || 0}
          matchedSkills={result.matched_skills || []}
          missingSkills={result.missing_skills || []}
        />

        {/* Resume Preview */}
        <PreviewCard preview={result.resume_preview} />

      </div>
    </section>
  );
}