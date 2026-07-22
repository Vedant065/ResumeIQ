interface MissingKeywordsCardProps {
  keywords: string[];
}

export default function MissingKeywordsCard({
  keywords,
}: MissingKeywordsCardProps) {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-lg">
      <h2 className="mb-5 text-xl font-bold text-red-700">
        ❌ Missing Keywords
      </h2>

      {keywords.length === 0 ? (
        <p className="text-gray-500">No missing keywords.</p>
      ) : (
        <div className="flex flex-wrap gap-2">
          {keywords.map((keyword, index) => (
            <span
              key={index}
              className="rounded-full bg-red-100 px-3 py-1 text-red-700"
            >
              {keyword}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}