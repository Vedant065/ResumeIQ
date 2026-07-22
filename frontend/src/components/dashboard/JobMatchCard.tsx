import { CheckCircle, XCircle } from "lucide-react";

interface Props {
  matchScore: number;
  matchedSkills: string[];
  missingSkills: string[];
}

export default function JobMatchCard({
  matchScore,
  matchedSkills,
  missingSkills,
}: Props) {
  return (
    <div className="rounded-3xl bg-white p-6 shadow-xl border">
      <h2 className="text-2xl font-bold mb-6">
        🎯 Job Description Match
      </h2>

      {/* Match Score */}
      <div className="mb-6">
        <div className="text-5xl font-bold text-blue-600">
          {matchScore}%
        </div>
        <p className="text-gray-500">
          Resume Match Score
        </p>
      </div>

      {/* Matched Skills */}
      <div className="mb-6">
        <h3 className="font-semibold mb-3">
          ✅ Matched Skills
        </h3>

        <div className="flex flex-wrap gap-2">
          {matchedSkills.length > 0 ? (
            matchedSkills.map((skill) => (
              <span
                key={skill}
                className="rounded-full bg-green-100 px-3 py-1 text-sm text-green-700"
              >
                <CheckCircle size={14} className="inline mr-1" />
                {skill}
              </span>
            ))
          ) : (
            <p className="text-gray-400">
              No matching skills found.
            </p>
          )}
        </div>
      </div>

      {/* Missing Skills */}
      <div>
        <h3 className="font-semibold mb-3">
          ❌ Missing Skills
        </h3>

        <div className="flex flex-wrap gap-2">
          {missingSkills.length > 0 ? (
            missingSkills.map((skill) => (
              <span
                key={skill}
                className="rounded-full bg-red-100 px-3 py-1 text-sm text-red-700"
              >
                <XCircle size={14} className="inline mr-1" />
                {skill}
              </span>
            ))
          ) : (
            <p className="text-gray-400">
              Great! No missing skills.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}