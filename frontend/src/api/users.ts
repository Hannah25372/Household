const API_URL = "http://localhost:8000/api";

export type User = {
  id: number;
  name: string;
  email: string;
  role: string;
};

export type CreateUserRequest = {
  name: string;
  email: string;
  role: string;
};


export type PaginatedResponse<T> = {
  items: T[];
  page: number;
  page_size: number;
  total: number;
};

export async function getUsers(
  page: number = 1,
  pageSize: number = 20,
): Promise<PaginatedResponse<User>> {
  const response = await fetch(
    `${API_URL}/users/?page=${page}&page_size=${pageSize}`,
  );

  if (!response.ok) {
    throw new Error("Failed to fetch users");
  }

  return response.json();
}


export async function createUser(
  user: CreateUserRequest,
): Promise<User> {
  const response = await fetch(`${API_URL}/users/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  });

  if (!response.ok) {
    throw new Error("Failed to create user");
  }

  return response.json();
}