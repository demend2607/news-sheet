export type Incident = {
  id: number;
  title: string;
  description: string | null;
  date: string;
  images: string;
  link: string;
  categories: string;
  color: string | null;
};

export type GetIncidentsParams = {
  limit?: number;
  offset?: number;
  sort_by?: "date" | "id" | "title";
  order?: "asc" | "desc";
};
