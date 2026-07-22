interface SuggestionCardProps {
  suggestions: string[];
}

export default function SuggestionCard({
  suggestions,
}: SuggestionCardProps) {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-lg">
      <h2 className="mb-5 text-xl font-bold text-blue-700">
        💡 Suggestions
      </h2>

      {suggestions.length === 0 ? (
        <p className="text-gray-500">
          Resume looks good!
        </p>
      ) : (
        <ul className="space-y-3">
          {suggestions.map((item, index) => (
            <li
              key={index}
              className="rounded-lg bg-blue-50 p-3"
            >
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}