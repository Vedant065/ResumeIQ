import { CircularProgressbar } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

interface Props {
  score: number;
}

export default function ATSGauge({ score }: Props) {
  const color =
    score >= 80
      ? "#16a34a"
      : score >= 60
      ? "#f59e0b"
      : "#ef4444";

  return (
    <div className="rounded-2xl bg-white shadow-lg p-8 text-center">
      <h2 className="text-3xl font-bold mb-8">
        ATS Compatibility Score
      </h2>

      <div className="w-56 h-56 mx-auto">
        <CircularProgressbar
          value={score}
          text={`${score}%`}
          styles={{
            path: {
              stroke: color,
            },
            text: {
              fill: color,
              fontSize: "18px",
              fontWeight: "bold",
            },
          }}
        />
      </div>

      <p className="mt-6 text-gray-600">
        Recruiter ATS Compatibility
      </p>
    </div>
  );
}