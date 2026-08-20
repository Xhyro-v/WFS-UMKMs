import api from "@/api/axios";

export async function getSummary() {
  const response = await api.get("/admin/dashboard/summary/Menu")

  return response.data;
}