import { notFound } from "next/navigation";

import { getIncidentsById } from "@/entities/incidents/api/get_incidents_byid";
import { getDate } from "@/shared/lib/hooks/utils";
import PageWithSidebar from "@/components/side-bar/PageWithSideBar";

export default async function IncidentDetailsPage({ params }: { params: Promise<{ id: string }> }) {
  const { id: rawId } = await params;
  const id = Number(rawId);

  if (!Number.isInteger(id) || id <= 0) return notFound();

  try {
    const incident = await getIncidentsById(id);
    const date = getDate(incident.date);

    return (
      <PageWithSidebar>
        <section className="wrapper py-8">
          <h1 className="text-2xl font-bold mb-4">{incident.title}</h1>
          <p className="text-sm text-gray-500 mb-6">
            {date.localTime}, {date.day}.{date.month}.{date.year}
          </p>
          <p className="mb-6">{incident.description}</p>
          {incident.images ? <img src={incident.images} alt={incident.title} className="w-full max-w-3xl rounded" /> : null}
        </section>
      </PageWithSidebar>
    );
  } catch {
    notFound();
  }
}
