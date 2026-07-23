import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export async function uploadResume(
  file: File,
  jobDescription: string
) {
  const formData = new FormData();

  formData.append("file", file);
  formData.append("job_description", jobDescription);

  const response = await API.post("/analyze", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
}
