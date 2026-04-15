import { api } from "@/shared/api/api-client";
import { GetIncidentsParams, Incident } from "../model/types";

export async function getIncidentsById(id: number): Promise<Incident> {
  return api.get<Incident>(`/v1/incidents/${id}`);
}
