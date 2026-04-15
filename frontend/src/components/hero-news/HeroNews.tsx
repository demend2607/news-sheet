import { getIncidents } from "@/entities/incidents/api/get_incidents";
import HeroCard from "./HeroCard";

export default async function HeroNews() {
  const incidents = await getIncidents({ limit: 4, offset: 0, sort_by: "date", order: "desc" });

  return (
    <div className="lg:col-span-8">
      <div className="space-y-6">
        {incidents.map((incident) => (
          <HeroCard key={incident.id} incident={incident} />
        ))}
      </div>
    </div>
  );
}
