import { SupabaseClient, User } from "@supabase/supabase-js";
import { Ref } from "nuxt/dist/app/compat/capi";

export const getProfile = async (
  userId: string,
  supabase: SupabaseClient
): Promise<any> => {
  let { data } = await supabase
    .from("profiles")
    .select(`username, website, avatar_url`)
    .eq("id", userId)
    .single();
  return data;
};

export const downloadImage = async (
  path: Ref,
  src: Ref,
  supabase: SupabaseClient
) => {
  try {
    const { data, error } = await supabase.storage
      .from("avatars")
      .download(path.value);
    console.log("Downloaded image path: ", path.value);
    console.log("Downloaded image: ", data);
    if (error) throw error as any;
    src.value = URL.createObjectURL(data);
  } catch (error) {
    console.error("Error downloading image: ", error.message);
  }
};

export const signOut = async (supabase: SupabaseClient) => {
  try {
    let { error } = await supabase.auth.signOut();
    if (error) throw error;
  } catch (error) {
    alert(error.message);
  }
};

export const updateProfile = async (
  userId: string,
  username: string,
  email: string,
  website: string,
  avatar_url: string,
  supabase: SupabaseClient
) => {
  try {
    const updates = {
      id: userId,
      username: username,
      website: website,
      avatar_url: avatar_url,
      email: email,
      updated_at: new Date(),
    };
    console.log("updates: ", updates);
    let { error } = await supabase.from("profiles").upsert(updates);
    if (error) throw error;
    console.log("updates: ", updates);
  } catch (error) {
    alert(error.message);
  }
};
