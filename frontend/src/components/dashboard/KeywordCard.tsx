interface Props {
  keywords: string[];
}

export default function KeywordCard({ keywords }: Props) {
  return (
    <div className="rounded-2xl bg-white border shadow-lg p-6">
      <h2 className="text-xl font-bold mb-5">
        📌 Keywords Found
      </h2>

      <div className="flex flex-wrap gap-3">
        {keywords.length > 0 ? (
          keywords.map((keyword, index) => (
            <span
              key={index}
              className="rounded-full bg-blue-100 px-4 py-2 text-blue-700 font-medium"
            >
              {keyword}
            </span>
          ))
        ) : (
          <p className="text-gray-500">
            No keywords found.
          </p>
        )}
      </div>
    </div>
  );
}