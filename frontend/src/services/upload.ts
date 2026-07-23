import axios from "axios";

export const uploadResume = async (formData: FormData) => {
  return axios.post(
    "http://localhost:8000/analyze",
    formData
  );
};

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
