interface PreviewCardProps {
  preview: string;
}

export default function PreviewCard({
  preview,
}: PreviewCardProps) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow">
      <h2 className="mb-4 text-xl font-bold">
        Resume Preview
      </h2>

      <pre className="whitespace-pre-wrap text-gray-700">
        {preview}
      </pre>
    </div>
  );
}