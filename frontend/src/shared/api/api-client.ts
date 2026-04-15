import { env } from "@/shared/config/env";

type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

interface RequestConfig extends Omit<RequestInit, "method" | "body"> {
  params?: Record<string, string | number | boolean | undefined>;
  body?: any;
}

export class ApiClient {
  constructor(
    private baseUrl: string,
    private defaultHeaders: HeadersInit = { "Content-Type": "application/json" },
  ) {}

  private async request<T>(method: HttpMethod, path: string, body?: any, config?: RequestConfig): Promise<T> {
    let url = `${this.baseUrl}${path}`;

    if (config?.params) {
      const searchParams = new URLSearchParams();
      Object.entries(config.params).forEach(([k, v]) => {
        if (v != null) searchParams.set(k, String(v));
      });
      const qs = searchParams.toString();
      if (qs) url += `?${qs}`;
    }

    const response = await fetch(url, {
      method,
      headers: { ...this.defaultHeaders, ...config?.headers },
      body: body ? JSON.stringify(body) : undefined,
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`API ${response.status}: ${errorText.slice(0, 200)}`);
    }
    if (response.status === 204) return undefined as T;

    return response.json();
  }

  get<T>(path: string) {
    return this.request<T>("GET", path);
  }

  // update<T>(path: string, body: any) {
  //   return this.request<T>("PUT", path, body);
  // }
}

export const api = new ApiClient(env.API_BASE);
