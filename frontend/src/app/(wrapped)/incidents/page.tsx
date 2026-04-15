import HeroCard from "@/components/hero-news/HeroCard";
import PageWithSidebar from "@/components/side-bar/PageWithSideBar";
import { getIncidents } from "@/entities/incidents/api/get_incidents";

export default async function IncidentsPage() {
  const incidents = await getIncidents({ limit: 20, offset: 0, sort_by: "date", order: "desc" });
  return (
    <PageWithSidebar>
      <h2 className="mb-4">Происшествия</h2>
      {incidents.map((incident) => (
        <HeroCard key={incident.id} incident={incident} />
      ))}
    </PageWithSidebar>
  );
}
