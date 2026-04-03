import { api } from "@/shared/api/api-client";
import { Incident, GetIncidentsParams } from "../model/types";

export async function getIncidents(params: GetIncidentsParams = {}): Promise<Incident[]> {
  // default values are the same as in the backend
  const search = new URLSearchParams({
    limit: String(params.limit ?? 20),
    offset: String(params.offset ?? 0),
    sort_by: params.sort_by ?? "date",
    order: params.order ?? "desc",
  });

  return api.get<Incident[]>(`/incidents?${search.toString()}`);
}
