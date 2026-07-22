import { Button } from "@/components/ui/button";
import { FileText } from "lucide-react";

export default function Navbar() {
  const scrollToSection = (id: string) => {
    document.getElementById(id)?.scrollIntoView({
      behavior: "smooth",
    });
  };

  return (
    <header className="sticky top-0 z-50 border-b bg-white/80 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        {/* Logo */}
        <div
          className="flex cursor-pointer items-center gap-2"
          onClick={() => scrollToSection("home")}
        >
          <FileText className="h-7 w-7 text-blue-600" />
          <h1 className="text-2xl font-bold text-blue-600">
            ResumeIQ
          </h1>
        </div>

        {/* Navigation */}
        <nav className="hidden items-center gap-8 md:flex">
          <button
            onClick={() => scrollToSection("home")}
            className="hover:text-blue-600"
          >
            Home
          </button>

          <button
            onClick={() => scrollToSection("features")}
            className="hover:text-blue-600"
          >
            Features
          </button>

          <button
            onClick={() => scrollToSection("about")}
            className="hover:text-blue-600"
          >
            About
          </button>
        </nav>

        <Button
          onClick={() => scrollToSection("upload-section")}
        >
          Upload Resume
        </Button>
      </div>
    </header>
  );
}