import Image from "next/image";

import Carousel from "@/modules/blog/ui/carousel/Carousel";
import Container from "@/shared/ui/Container";

export default function Home() {
  return (
    <section>
      <Carousel />
      <Container>HEROO</Container>
    </section>
  );
}
