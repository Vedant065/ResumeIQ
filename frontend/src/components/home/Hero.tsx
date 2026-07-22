import { Button } from "@/components/ui/button";

export default function Hero() {
  const scrollToSection = (id: string) => {
    document.getElementById(id)?.scrollIntoView({
      behavior: "smooth",
    });
  };

  return (
    <section className="mx-auto max-w-7xl px-6 py-24 text-center">
      <h1 className="text-5xl font-extrabold leading-tight">
        Analyze Your Resume
        <br />
        <span className="text-blue-600">with AI in Seconds</span>
      </h1>

      <p className="mx-auto mt-6 max-w-2xl text-lg text-gray-600">
        Get an ATS score, AI-powered suggestions, keyword analysis,
        and actionable improvements to land more interviews.
      </p>

      <div className="mt-10 flex justify-center gap-4">
        <Button
          size="lg"
          onClick={() => scrollToSection("upload-section")}
        >
          Upload Resume
        </Button>

        <Button
          variant="outline"
          size="lg"
          onClick={() => scrollToSection("features")}
        >
          Learn More
        </Button>
      </div>
    </section>
  );
}