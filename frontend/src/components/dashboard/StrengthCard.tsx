interface StrengthCardProps {
  strengths: string[];
}

export default function StrengthCard({
  strengths,
}: StrengthCardProps) {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-lg">
      <h2 className="mb-5 text-xl font-bold text-green-700">
        ✅ Strengths
      </h2>

      {strengths.length === 0 ? (
        <p className="text-gray-500">
          No strengths detected.
        </p>
      ) : (
        <div className="flex flex-wrap gap-3">
          {strengths.map((strength, index) => (
            <span
              key={index}
              className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700"
            >
              {strength}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}