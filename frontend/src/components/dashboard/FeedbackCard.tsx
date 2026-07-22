interface FeedbackCardProps {
  feedback: string;
}

export default function FeedbackCard({
  feedback,
}: FeedbackCardProps) {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-lg">
      <h2 className="mb-5 text-xl font-bold text-purple-700">
        🤖 AI Feedback
      </h2>

      <p className="whitespace-pre-wrap text-gray-700 leading-7">
        {feedback ||
          "AI feedback is currently unavailable."}
      </p>
    </div>
  );
}