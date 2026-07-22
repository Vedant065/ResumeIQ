import Navbar from "@/components/layout/Navbar";
import Hero from "@/components/home/Hero";
import UploadCard from "@/components/home/UploadCard";
import Features from "@/components/home/Features";
import Footer from "@/components/layout/Footer";

export default function Home() {
  return (
    <div id="home" className="min-h-screen bg-slate-50">
      <Navbar />
      <Hero />
      <UploadCard />
      <Features />
      <Footer />
    </div>
  );
}