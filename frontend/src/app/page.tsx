import { getIncidents } from "@/entities/incidents/api/get_incidents";

import Carousel from "@/modules/home/carousel/ui/Carousel";
import HeroMain from "@/modules/home/hero-main/ui/HeroMain";

export default async function Home() {
  const incidents = await getIncidents({ limit: 4, offset: 0, sort_by: "date", order: "desc" });

  return (
    <>
      <Carousel incidents={incidents} />
      <HeroMain />
    </>
  );
}
