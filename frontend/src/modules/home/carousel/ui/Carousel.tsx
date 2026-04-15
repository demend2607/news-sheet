"use client";

import useEmblaCarousel from "embla-carousel-react";
import { ChevronLeftIcon, ChevronRightIcon } from "@radix-ui/react-icons";

import CarouselSlide from "./CarouselSlide";
import { Incident } from "@/entities/incidents/model/types";

import "./carousel.css";

export default function Carousel({ incidents }: { incidents: Incident[] }) {
  const [emblaRef, emblaApi] = useEmblaCarousel({
    loop: true,
  });

  const goToPrev = () => emblaApi?.scrollPrev();
  const goToNext = () => emblaApi?.scrollNext();

  return (
    <section id="main__banner">
      <div className="embla">
        <div className="embla__viewport" ref={emblaRef}>
          <div className="embla__container">
            {incidents.map((incident) => (
              <CarouselSlide key={incident.id} incident={incident} />
            ))}
          </div>
        </div>
        <div className="embla__buttons">
          <button className="embla__prev embla__button" onClick={goToPrev}>
            <ChevronLeftIcon />
          </button>
          <button className="embla__next embla__button" onClick={goToNext}>
            <ChevronRightIcon />
          </button>
        </div>
      </div>
    </section>
  );
}
