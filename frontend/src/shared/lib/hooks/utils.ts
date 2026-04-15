import { twMerge } from "tailwind-merge";
import clsx, { ClassValue } from "clsx";
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
export async function sleep(ms: number) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

export function getDate(date: string) {
  const newDate = new Date(date);

  const day = newDate.getDate().toString().padStart(2, "0");
  const month = (newDate.getMonth() + 1).toString().padStart(2, "0");
  const year = newDate.getFullYear().toString();
  const localTime = newDate.toLocaleString("RU-ru", { hour: "2-digit", minute: "2-digit" });

  return { day, month, year, localTime };
}
