"use client";

import useEmblaCarousel from "embla-carousel-react";
import { ChevronLeftIcon, ChevronRightIcon } from "@radix-ui/react-icons";

import "./carousel.css";

export default function Carousel() {
  const [emblaRef, emblaApi] = useEmblaCarousel({
    loop: true,
  });

  const goToPrev = () => emblaApi?.scrollPrev();
  const goToNext = () => emblaApi?.scrollNext();

  return (
    <div className="embla">
      <div className="embla__viewport" ref={emblaRef}>
        <div className="embla__container">
          <div className="embla__slide">
            <div className="carousel__item">
              <div className="post__category">Category</div>
              <div className="post__link">
                <a href="/">Link to post</a>
              </div>
              <ul className="post__info">
                <li>autor</li>
                <li>data</li>
                <li>comments</li>
              </ul>
            </div>
          </div>
          <div className="embla__slide"></div>
          <div className="embla__slide"></div>
          <div className="embla__slide"></div>
          <div className="embla__slide"></div>
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
  );
}
