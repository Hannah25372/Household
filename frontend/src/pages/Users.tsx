import { useState } from "react";
import { useEffect, useRef } from "react";
import { LuTrash, LuUserPlus, LuX, LuCheck } from "react-icons/lu";
import { getUsers, createUser, type CreateUserRequest, type User, deleteUser } from "../api/users";
import Pagination from "../components/Pagination";

function UserHeader() {
  return (
    <div>
      <h1>Users</h1>
    </div>
  );
}

function AddUserModal({
  onCancel,
  onSubmit,
}: {
  onCancel: () => void;
  onSubmit: (user: CreateUserRequest) => void;
}) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");
  const dialogRef = useRef<HTMLDialogElement>(null);

  const handleRoleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRole(event.target.value);
  };
  
  function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    onSubmit({
      name,
      email,
      role,
    });
  }

  useEffect(() => {
    dialogRef.current?.showModal();
  }, []);

  return (
    <dialog ref={dialogRef} className="add-user-modal">
      <h2>Add User</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-field">
          <label htmlFor="userName">Name</label>
          <input id="userName" type="text" value={name} onChange={(event) => setName(event.target.value)}/>
        </div>

        <div className="form-field">
          <label htmlFor="userEmail">Email</label>
          <input id="userEmail" type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
        </div>

        <div className="form-field">
          <label htmlFor="userRole">Role</label>
          <div className="radio-group">
            <label>
              <input id="userRole" type="radio" name="role" value="user" checked={role === "user"} onChange={handleRoleChange}/>
              User
            </label>
            <label>
              <input id="adminRole" type="radio" name="role" value="admin" checked={role === "admin"} onChange={handleRoleChange}/>
              Admin
            </label>
          </div>
        </div>

        <button type="button" onClick={onCancel}><LuX/></button>
        <button type="submit"><LuCheck/></button>
      </form>
    </dialog>
  );
}

function TableControls({ onAddUser }: { onAddUser: () => void }) {
  return (
    <div className="table-controls">
      <div className="table-filters">
        {/* filters here */}
      </div>
      <div className="table-actions">
       <button onClick={onAddUser}><LuUserPlus/></button>
      </div>
    </div>
  );
}

function UserTable({ users, onDeleteUser }: { users: User[], onDeleteUser: (user_id:number) => void }) {
  return (
    <div className="table-container">
      <table className="data-table">
        <thead>
          <tr>
            <th>User ID</th>
            <th>User Name</th>
            <th>User Email</th>
            <th>User Role</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td>{user.role}</td>
              <td><button onClick={() => onDeleteUser(user.id)}><LuTrash/></button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function Users() {
  const [users, setUsers] = useState<User[]>([]);
  const [showAddUserModal, setShowAddUserModal] = useState(false);
  const [page, setPage] = useState(1);
  const [total, setTotal] = useState(0);
  const pageSize = 20;

  //getting users list
  useEffect(() => {
    async function loadUsers() {
      const data = await getUsers(page, pageSize);
      setUsers(data.items);
      setTotal(data.total);
    }
    loadUsers();
  }, [page]);

  //create user function
  async function handleCreateUser(
    user: CreateUserRequest,
  ) {
    try {
      const newUser = await createUser(user);
      setUsers((currentUsers) => [
        ...currentUsers,
        newUser,
      ]);
      setShowAddUserModal(false);
    } catch (error) {
      console.error(error);
    }
  }

  //delete user function
  async function handleDeleteUser(
    user_id: number,
  ) {
    try {
      await deleteUser(user_id);
      setUsers(users => users.filter(user => user.id !== user_id));
      setTotal(total => total - 1);
    } catch (error) {
      console.error(error)
    }
  };

  return (
    <div className="page-container">
      <UserHeader/>
      <div className="table-section">
        <TableControls onAddUser={() => setShowAddUserModal(true)}/>
        <UserTable users={users} onDeleteUser={handleDeleteUser}/>
        <Pagination
          page={page}
          pageSize={pageSize}
          total={total}
          onPageChange={setPage}
        />
      </div>
      {showAddUserModal && (
        <AddUserModal
          onCancel={() => setShowAddUserModal(false)}
          onSubmit={handleCreateUser}
        />
      )}
    </div>
  );
}

export default Users;