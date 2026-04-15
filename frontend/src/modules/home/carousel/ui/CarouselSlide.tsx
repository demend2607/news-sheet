"use client";

import Link from "next/link";

import { Incident } from "@/entities/incidents/model/types";
import { ClockIcon } from "@radix-ui/react-icons";

export default function CarouselSlide({ incident }: { incident: Incident }) {
  const category = {
    category: incident.categories === "incidents" ? "Происшествия" : "Новости",
    city: "Хабаровск",
  };

  const date = new Date(incident.date);

  const formateDate = {
    day: date.getDate(),
    month: date.toLocaleString("RU-ru", { month: "short" }),
    year: date.getFullYear().toString(),
    localTime: date.toLocaleString("RU-ru", { hour: "2-digit", minute: "2-digit" }),
  };
  return (
    <div className="embla__slide relative">
      <div className="absolute inset-0 bg-cover bg-center blur-xs brightness-70" style={{ backgroundImage: `url(${incident.images})` }}></div>
      <div className="relative carousel__item text-white drop-shadow-lg font-medium">
        <div className="post__category">{category.category}</div>
        <div className="post__title">{incident.title}</div>
        <div className="post__link">
          <Link href={`/incidents/${incident.id}`}>Подробнее</Link>
        </div>
        <ul className="post__info">
          <li className="gap-1 flex! items-center!">
            <ClockIcon />
            {formateDate.day} {formateDate.month}
          </li>
        </ul>
      </div>
    </div>
  );
}
