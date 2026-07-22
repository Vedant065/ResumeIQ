import { Brain, CheckCircle, FileSearch, Download } from "lucide-react";

const features = [
  {
    title: "ATS Score",
    icon: CheckCircle,
    desc: "Get an instant ATS compatibility score."
  },
  {
    title: "AI Suggestions",
    icon: Brain,
    desc: "Improve your resume using Gemini AI."
  },
  {
    title: "Keyword Analysis",
    icon: FileSearch,
    desc: "Find missing keywords recruiters expect."
  },
  {
    title: "PDF Report",
    icon: Download,
    desc: "Download a complete resume analysis."
  }
];

export default function Features() {
  return (
    <section
      id="features"
      className="mx-auto mt-24 max-w-7xl px-6"
    >
      <h2 className="text-center text-4xl font-bold">
        Why ResumeIQ?
      </h2>

      <div className="mt-14 grid gap-8 md:grid-cols-2 lg:grid-cols-4">
        {features.map((feature) => {
          const Icon = feature.icon;

          return (
            <div
              key={feature.title}
              className="rounded-xl border bg-white p-6 shadow hover:shadow-lg transition"
            >
              <Icon className="mb-4 h-10 w-10 text-blue-600" />

              <h3 className="text-xl font-semibold">
                {feature.title}
              </h3>

              <p className="mt-2 text-gray-600">
                {feature.desc}
              </p>
            </div>
          );
        })}
      </div>
    </section>
  );
}