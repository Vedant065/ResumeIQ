import { useState, useEffect, useRef } from "react";
import { useDropzone } from "react-dropzone";
import { Upload, FileText } from "lucide-react";

import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { uploadResume } from "@/services/upload";
import Dashboard from "@/components/dashboard/Dashboard";

export default function UploadCard() {
  const [fileName, setFileName] = useState("");
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [jobDescription, setJobDescription] = useState("");

  const dashboardRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (result) {
      dashboardRef.current?.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  }, [result]);

  const onDrop = async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0];

    if (!file) return;

    setFileName(file.name);
    setLoading(true);

    try {
      // Pass both file and job description
      const response = await uploadResume(file, jobDescription);
      setResult(response);
    } catch (error) {
      console.error(error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: {
      "application/pdf": [".pdf"],
    },
    multiple: false,
  });

  return (
    <>
      <section id="upload-section" className="mx-auto mt-16 max-w-5xl px-6">
        <Card className="rounded-3xl border-2 border-dashed border-blue-300 bg-white shadow-xl transition-all duration-300 hover:-translate-y-1 hover:border-blue-500 hover:shadow-2xl">
          <CardContent className="py-16">

            {/* Upload Area */}
            <div
              {...getRootProps()}
              className="cursor-pointer text-center"
            >
              <input {...getInputProps()} />

              <div className="mx-auto flex h-24 w-24 items-center justify-center rounded-full bg-gradient-to-br from-blue-500 to-indigo-600 shadow-lg">
                <Upload className="h-12 w-12 text-white" />
              </div>

              <h2 className="mt-6 text-3xl font-bold">
                Upload Your Resume
              </h2>

              <p className="mt-3 text-gray-600">
                Drag & Drop your PDF here or click to browse.
              </p>

              <Button className="mt-8 rounded-xl bg-blue-600 px-8 py-6 text-lg hover:bg-blue-700">
                <FileText className="mr-2 h-5 w-5" />
                Choose PDF
              </Button>

              {fileName && (
                <p className="mt-4 font-medium text-blue-600">
                  Selected: {fileName}
                </p>
              )}
            </div>

            {/* Job Description */}
            <div className="mt-10">
              <label className="mb-2 block text-left text-lg font-semibold text-slate-700">
                Job Description (Optional)
              </label>

              <textarea
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
                rows={8}
                placeholder="Paste the job description here..."
                className="w-full rounded-xl border border-slate-300 p-4 focus:border-blue-500 focus:outline-none"
              />
            </div>

            {/* Loading */}
            {loading && (
              <div className="mt-8 flex flex-col items-center">
                <div className="h-10 w-10 animate-spin rounded-full border-4 border-blue-500 border-t-transparent"></div>

                <p className="mt-4 text-lg font-medium text-gray-600">
                  Analyzing your resume...
                </p>

                <p className="text-sm text-gray-400">
                  This may take a few seconds.
                </p>
              </div>
            )}
          </CardContent>
        </Card>
      </section>

      {result && (
        <div ref={dashboardRef}>
          <Dashboard result={result} />
        </div>
      )}
    </>
  );
}