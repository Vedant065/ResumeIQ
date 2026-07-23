import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export const uploadResume = async (formData: FormData) => {
  return axios.post(
    `${API_URL}/analyze`,
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
